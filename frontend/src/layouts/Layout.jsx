import React from 'react';

import { Outlet, useMatches, Link as RouterLink } from 'react-router-dom';
import { Paper, Grid, Breadcrumbs, Link } from '@mui/material';
import BCBox from 'components/BCBox';
import AppNavbar from 'components/Navbars/AppNavbar';
import NavigateNextIcon from '@mui/icons-material/NavigateNext';

const Layout = () => {
  const matches = useMatches();
  const crumbs = matches
    .filter(match => Boolean(match.handle?.crumb))
    .map(match => ({
      label: match.handle.crumb(match.data),
      path: match.pathname,
    }));

  return (
    <>
      <Grid container
        rowSpacing={2}
        sx={{
          margin: "0",
          padding: "1rem",
          background: "background.paper",
        }}
        columnSpacing={{ xs: 1, sm: 1, md: 1 }}
      >
        <Grid item xs={12}
          sx={{
            maxHeight: "20vh",
            position: "relative",
            top: 0,
            zIndex: 10, // Adjust the z-index if needed
          }}
        >
          <AppNavbar
            title="Low Carbon Fuel Standard"
            balance="50,000"
            organizationName="BC Government"
          />
        </Grid>
        <Grid item my={12} lg={12}>
          <BCBox>
            <Paper p={2} elevation={5} sx={{ padding: "1rem", minHeight: '5vh' }}>
              <Breadcrumbs separator={<NavigateNextIcon fontSize="small" />}>
                {crumbs.map((crumb, index) =>
                  index + 1 !== crumbs.length ? (
                    <Link
                      key={crumb.path}
                      component={RouterLink}
                      to={crumb.path}
                      disabled={true}
                    >
                      {crumb.label}
                    </Link>
                  ) : (
                    <span key={crumb.path}>{crumb.label}</span>
                  ),
                )}
              </Breadcrumbs>
            </Paper>
            <BCBox py={4}>
              <Outlet />
            </BCBox>
          </BCBox>
        </Grid>
      </Grid>
    </>
  );
};
export default Layout;
